export const trackTypeList = [
  {
    label: '模型类型',
    options: [
      {
        value: 'YOLOv8',
        label: '原模型'
      },
      {
        value: 'YOLOv8+small_target',
        label: '原模型+小目标检测头'
      },
      {
        value: 'final_model',
        label: '组合优化模型'
      }
    ]
  }
]

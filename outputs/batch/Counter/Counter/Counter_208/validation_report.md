# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_208`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_208/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [26–37], lower_priority='Action_DownBlock' annotated_start=28, effective_Action_DownBlock_start=38.
> - Action 'Action_None' range [26-111] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-180] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [28-53] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-48] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [28-100] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-165] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-74] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-52] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-70] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-111] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-122] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [38-52] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [59-66] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [119-180] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-37] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-65] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [34-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-109] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-42] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-51] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-93] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-126] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-151] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [71-77] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-128] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-76] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-167] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-128] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-149] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '29' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
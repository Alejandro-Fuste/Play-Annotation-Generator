# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_308`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_308/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Deduplicated duplicate event 'Action_DownBlock' at frame 61 for track '2'.
> - Action 'Action_None' range [58-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-108] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [61-86] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [61-74] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-80] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-128] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-134] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-113] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [95-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-71] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-116] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-74] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-152] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [62-64] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [80-83] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [103-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [113-120] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-176] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-12] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-22] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-62] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-83] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-98] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-132] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [65-66] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [68-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [88-106] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-94] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-189] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '27' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_129`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_129/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [61–75], lower_priority='Action_DownBlock' annotated_start=63, effective_Action_DownBlock_start=76.
> - Action 'Action_None' range [61-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-196] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-133] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-81] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-101] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-210] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [61-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [63-118] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-80] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [63-88] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-81] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-188] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [63-92] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [102-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-136] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [96-197] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [76-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [87-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-138] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-112] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-189] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '31' has 1 frames without a visible bounding box.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
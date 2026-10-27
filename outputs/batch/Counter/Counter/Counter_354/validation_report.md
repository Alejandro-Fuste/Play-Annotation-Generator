# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_354`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_354/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallCarry' for track '4' has invalid range: start=62, end=60. Clamping end to start.
> - Action 'Action_None' range [21-108] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-150] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-155] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-106] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-120] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-108] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [24-30] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [34-72] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [93-94] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-55] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [21-68] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [24-112] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-139] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-148] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-36] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-155] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-138] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-158] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-166] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-180] for track '22' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_23`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_23/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [10–24], lower_priority='Action_PassBlock' annotated_start=13, effective_Action_PassBlock_start=25.
> - Action 'Action_None' range [10-86] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-113] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-86] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-101] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-44] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-131] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [24-121] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [126-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-73] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-85] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-101] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-27] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-64] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-29] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-41] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-47] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-115] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [119-136] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-44] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [48-53] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [55-127] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [99-124] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-34] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-30] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-46] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-51] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-50] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-69] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-128] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-78] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-135] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-82] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-130] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-120] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-105] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-133] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-146] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-157] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-179] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-139] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '32' has 1 frames without a visible bounding box.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
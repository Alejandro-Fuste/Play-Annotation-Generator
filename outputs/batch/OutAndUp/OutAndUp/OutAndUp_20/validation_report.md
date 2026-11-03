# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_20`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_20/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [22-167] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-211] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-174] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-112] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-264] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SellOut' range [55-84] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [85-125] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-62] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-248] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-127] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-221] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-80] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-200] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-144] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [93-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [97-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '16' starts at frame 22, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [22-22] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-26] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-119] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-152] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-118] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-97] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-157] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-224] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-253] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-104] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-167] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [171-222] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-112] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-174] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-199] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-216] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-232] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-252] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-258] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-135] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-233] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-204] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-219] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-241] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-299] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-214] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-288] for track '31' has 1 frames without a visible bounding box.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
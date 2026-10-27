# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_251`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_251/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 504: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [73–88], lower_priority='Action_DownBlock' annotated_start=76, effective_Action_DownBlock_start=89.
> - Segment 'Action_DownBlock' for track '16' has invalid range: start=76, end=72. Clamping end to start.
> - Action 'Action_None' range [73-187] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-239] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-220] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-228] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-130] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-232] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [114-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-233] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-79] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-95] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-131] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [89-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-239] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-75] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [76-88] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [76-133] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-204] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-221] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [73-84] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-239] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-72] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-83] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-114] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-230] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-59] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [76-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [87-129] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-113] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-144] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-239] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-237] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-219] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-234] for track '26' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_140`
- **Input XML**: `outputs/batch/Power/Power/Power_140/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 282: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [7-241] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-269] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-174] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-192] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-269] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-216] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-164] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-43] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-46] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [162-214] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-42] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-167] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-171] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-218] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-11] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-11] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-158] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-195] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-218] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [162-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [186-188] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [211-216] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [240-267] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-179] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-115] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-254] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-264] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-131] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-143] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [162-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-158] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-167] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-182] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-226] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-218] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-230] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-203] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-231] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-244] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-261] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-268] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-250] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-258] for track '26' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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
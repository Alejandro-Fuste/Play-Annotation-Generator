# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_141`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_141/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-128] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-51] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-208] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [66-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [88-155] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [161-162] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [166-167] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-234] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-32] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-43] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-135] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-183] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-163] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-216] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-173] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-252] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-126] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-12] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-28] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-41] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-75] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-70] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-85] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-107] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-122] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-138] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-211] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-172] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-252] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-256] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-208] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-212] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-219] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-238] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-247] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-267] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
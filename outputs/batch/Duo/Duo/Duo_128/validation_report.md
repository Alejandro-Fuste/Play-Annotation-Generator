# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_128`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_128/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 328 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
> - Action 'Action_PreSnap' range [0-328] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-20] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-283] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [209-259] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-328] for track '7' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-246] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-287] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-263] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-304] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-323] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-211] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-177] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-304] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-313] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [209-259] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-304] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-319] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-283] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-202] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-220] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-196] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-202] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-244] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-102] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-110] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-328] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-149] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-300] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-317] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-208] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [209-259] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-280] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-292] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-256] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-266] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-294] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-317] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-276] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-280] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-268] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-327] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-280] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-278] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-322] for track '34' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
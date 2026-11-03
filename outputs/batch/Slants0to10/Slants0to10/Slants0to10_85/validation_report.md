# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_85`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_85/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 86: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Overlapping action conflict at frame 10 for track '13': 'Action_SnapReceive' vs 'Action_RunSlantRoute'. Overriding with 'Action_RunSlantRoute'.
> - Action 'Action_PreSnap' range [0-18] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-25] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-60] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-268] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-299] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-265] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-78] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-52] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-56] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-80] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-26] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-74] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [78-92] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-98] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [100-138] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-42] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-52] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-23] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [90-149] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [151-263] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [265-274] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [276-282] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-27] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-26] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-41] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [91-299] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-26] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-72] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-59] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-131] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-160] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-67] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-57] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-76] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-83] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-93] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-121] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-131] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-136] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-236] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-250] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-265] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-279] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-284] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-237] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-165] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-178] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-202] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-296] for track '34' has 2 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
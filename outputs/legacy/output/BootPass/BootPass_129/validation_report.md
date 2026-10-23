# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_129`
- **Input XML**: `output/BootPass/BootPass_129/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 49 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_ThrowPass' for track '10' has invalid range: start=127, end=71. Clamping end to start.
> - Segment 'Action_FakeHandoff' for track '17' has invalid range: start=67, end=62. Clamping end to start.
> - Segment 'Action_BootAway' for track '17' has invalid range: start=85, end=62. Clamping end to start.
> - Action 'Action_PreSnap' range [0-89] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-110] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-170] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-193] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-61] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-71] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-30] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-62] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-143] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-162] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-183] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-190] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-201] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-214] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-223] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-230] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-23] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-29] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-38] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-62] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-3] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-7] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-26] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-136] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-178] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-18] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-25] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-27] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-60] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-37] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-123] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-146] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-178] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-65] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-85] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-91] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-73] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-155] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-91] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-103] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-123] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-143] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-127] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-136] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-164] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-170] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-186] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-152] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-143] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-175] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-242] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-216] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-211] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-299] for track '33' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-262] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-291] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-246] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-270] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-291] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-299] for track '35' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
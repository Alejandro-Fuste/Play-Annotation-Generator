# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_7`
- **Input XML**: `output/BootPass/BootPass_7/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 6, Column 'Run Block': Could not parse frame number from '-' in entry '-,OL'.
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-233] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-286] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-190] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-204] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-230] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-194] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-282] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-159] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-187] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-206] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-217] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-277] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-221] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-78] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-98] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-118] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-154] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-160] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-165] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-170] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-101] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-109] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-190] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-198] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-228] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-214] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-228] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-224] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
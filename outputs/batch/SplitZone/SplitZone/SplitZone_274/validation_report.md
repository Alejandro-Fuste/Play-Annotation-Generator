# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `SplitZone_274`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_274/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 25 |
| Action Segments inferred | 99 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_BlockSecondLevel' at frame 115 targets track ID '134', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_BlockSecondLevel' for track '0' (DT2) duration 183 frames exceeds threshold 90 frames [start=115, end=297].
> - Validation warning: Action 'Action_BlockSecondLevel' for track '7' (DT1) duration 185 frames exceeds threshold 90 frames [start=115, end=299].
> - Action 'Action_PreSnap' range [0-114] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [116-117] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [119-287] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [292-297] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-263] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-135] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-184] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [137-284] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [287-292] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-233] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-245] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-139] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-148] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-160] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [115-245] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [247-259] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [263-280] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [282-283] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [285-296] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-288] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-177] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-190] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-240] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-224] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-232] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-231] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [275-287] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-236] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-148] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-129] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-190] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-235] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-280] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-288] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-109] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-136] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 156, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [156-156] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-171] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-292] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-167] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-143] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-140] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-241] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [244-296] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-270] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-294] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-259] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [254-283] for track '30' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
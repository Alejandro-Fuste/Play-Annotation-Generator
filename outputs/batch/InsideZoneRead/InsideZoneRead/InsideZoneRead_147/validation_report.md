# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_147`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_147/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 29 |
| Ball Tracks | 3 |
| CSV events parsed | 16 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '6' has invalid range: start=321, end=306. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '7' has invalid range: start=321, end=175. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '10' has invalid range: start=321, end=253. Clamping end to start.
> - Segment 'Action_BallSnap' for track '17' has invalid range: start=318, end=242. Clamping end to start.
> - Action 'Action_PreSnap' range [0-257] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-245] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-127] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-131] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-244] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-236] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-303] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-306] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-141] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-150] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-253] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-116] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-242] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-125] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-157] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-141] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-188] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-216] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-225] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-249] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-253] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-186] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-217] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-237] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-242] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-317] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-190] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-316] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-321] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-328] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-317] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-328] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-276] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-284] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-232] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-253] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '29' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Action event 'Action_SnapReceive' has invalid start frame 334. Video range is [0, 329].
> - Action event 'Action_ReadDefender' has invalid start frame 338. Video range is [0, 329].
> - Action event 'Action_BallCarry' has invalid start frame 363. Video range is [0, 329].
> - Action event 'Action_None' has invalid start frame 412. Video range is [0, 329].
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_147'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
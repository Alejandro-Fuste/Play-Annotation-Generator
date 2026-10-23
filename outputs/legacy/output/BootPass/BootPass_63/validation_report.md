# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_63`
- **Input XML**: `output/BootPass/BootPass_63/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 121 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-304] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-329] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-297] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-194] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-329] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-231] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-316] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-326] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-223] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-299] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-308] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-329] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-201] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-278] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-298] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-305] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-309] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-328] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-234] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-245] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-329] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-277] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-287] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-318] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-291] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-305] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-329] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-191] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-181] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-329] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-183] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-190] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-193] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-222] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-212] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-242] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-247] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-273] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-329] for track '30' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-272] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-329] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-304] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-307] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-320] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-329] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
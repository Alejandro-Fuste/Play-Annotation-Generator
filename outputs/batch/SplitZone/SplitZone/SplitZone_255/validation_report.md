# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_255`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_255/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_None' range [159-216] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-218] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-242] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [161-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-256] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-183] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-205] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-256] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [162-231] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [192-275] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '12' starts at frame 192, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [192-192] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [283-294] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-228] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-246] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-197] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-215] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-233] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-250] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [263-274] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-22] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-158] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-168] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-184] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-222] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-231] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-282] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [162-211] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [213-215] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-255] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-293] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [162-235] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-161] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [162-177] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [188-190] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [162-170] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-234] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [159-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-292] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-204] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-329] for track '23' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [224-260] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-253] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-258] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-329] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-279] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-284] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '30' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_182`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_182/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 114 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (LG) duration 92 frames exceeds threshold 90 frames [start=166, end=257].
> - Segment 'Action_Handoff' for track '12' has invalid range: start=181, end=171. Clamping end to start.
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (RT) duration 98 frames exceeds threshold 90 frames [start=166, end=263].
> - Action 'Action_None' range [163-247] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-250] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-395] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-255] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [166-178] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-190] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-215] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-232] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-267] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-56] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [166-219] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-241] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-41] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [166-198] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [200-210] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [213-217] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [219-253] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [256-257] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [168-169] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [174-234] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [224-239] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [242-243] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-13] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-25] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [169-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [166-182] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [199-208] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [215-216] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [219-245] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [247-249] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [251-263] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-15] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-17] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-205] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-217] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-62] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-76] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-86] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-177] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [183-188] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [192-200] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [212-213] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-85] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-229] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-244] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-263] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-276] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-247] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-259] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-199] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-224] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-256] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-250] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-234] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [272-278] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-246] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-285] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-297] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-275] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-303] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-292] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-300] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-312] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-328] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [339-341] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-385] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-331] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [336-339] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-341] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-361] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-379] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-383] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-404] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-378] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-382] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-410] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-387] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-389] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-409] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-414] for track '44' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
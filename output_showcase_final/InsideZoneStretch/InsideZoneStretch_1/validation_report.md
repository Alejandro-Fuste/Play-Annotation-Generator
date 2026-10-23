# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneStretch_1`
- **Input XML**: `output_showcase_final/InsideZoneStretch/InsideZoneStretch_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 158 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_None' range [182-380] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-378] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [232-265] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [273-274] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [278-331] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-342] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-346] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-369] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-229] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-419] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-260] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-298] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-366] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [386-387] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-230] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-280] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-314] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-419] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-16] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-27] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-311] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-331] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-376] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-246] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-322] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [191-194] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [203-220] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-246] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-265] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-325] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [328-338] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-346] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [348-350] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-412] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [415-417] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [182-190] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-187] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [191-197] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [199-203] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [206-208] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [210-211] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [224-243] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [248-261] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-346] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-309] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-419] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-200] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-316] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-339] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-355] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-384] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-389] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-254] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-419] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [191-192] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-43] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-186] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-192] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-243] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-26] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-126] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-142] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-384] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-287] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-312] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-334] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [336-337] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-272] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [274-285] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-291] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-390] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-243] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-375] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [377-381] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-259] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-293] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [297-307] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-325] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-341] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [343-347] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-387] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [390-391] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-292] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-301] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-307] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-319] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-339] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-347] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-355] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-393] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-396] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-382] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-395] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-410] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-405] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [411-416] for track '32' has 2 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
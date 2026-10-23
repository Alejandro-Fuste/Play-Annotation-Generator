# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneStretch_2`
- **Input XML**: `output_showcase_final/InsideZoneStretch/InsideZoneStretch_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 113 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 5: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_None' range [147-215] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-383] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-336] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [338-340] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-365] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-174] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-186] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [189-221] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-185] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-211] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-317] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-375] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [377-379] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-384] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-385] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-240] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-263] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [203-310] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [313-318] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [321-323] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-246] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-280] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-317] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-333] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-389] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [160-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-276] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-346] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [348-349] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-359] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-168] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-233] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-380] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-174] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-204] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-225] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-297] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-332] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-48] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-77] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-98] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-124] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-157] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [166-173] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-226] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-389] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-212] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-277] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-284] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-273] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-290] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-304] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-293] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-341] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [225-243] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-262] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-306] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-298] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-304] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-306] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-315] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-360] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [362-364] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-389] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-360] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [372-378] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-382] for track '27' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
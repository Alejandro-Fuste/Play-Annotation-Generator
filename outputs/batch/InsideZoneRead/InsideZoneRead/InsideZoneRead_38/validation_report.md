# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_38`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [62–74], lower_priority='Action_ZoneBlock' annotated_start=64, effective_Action_ZoneBlock_start=75.
> - Action 'Action_None' range [62-254] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [256-260] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-327] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-121] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-359] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-280] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-296] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-107] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-163] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-220] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [102-111] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-273] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-244] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-336] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-353] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-212] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-85] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-95] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-145] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-148] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-260] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-282] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-292] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-305] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-213] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-152] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-359] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [75-78] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-221] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-73] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-112] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-305] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-215] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-171] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-234] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-284] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-235] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-292] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-311] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-335] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-356] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-204] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-249] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-230] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-320] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [322-342] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-301] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [313-317] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [323-359] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [280-286] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-310] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-284] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-342] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-293] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-310] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-302] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [305-335] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-349] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-307] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-344] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-348] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-335] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [340-343] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-334] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-342] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-359] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-355] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-359] for track '35' has 1 frames without a visible bounding box.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
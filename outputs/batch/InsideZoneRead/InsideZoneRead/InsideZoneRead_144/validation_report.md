# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_144`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_144/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [122–136], lower_priority='Action_ZoneBlock' annotated_start=125, effective_Action_ZoneBlock_start=137.
> - Action 'Action_None' range [122-205] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-212] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-347] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-141] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-178] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-359] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-222] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-230] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [159-172] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [177-185] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [189-190] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-154] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-169] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [186-200] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-189] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-257] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-177] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-295] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [299-357] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-144] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-259] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [261-311] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-343] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-359] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-144] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-138] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-216] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-233] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [141-145] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-355] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-141] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-174] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-304] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-248] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-269] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-344] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-317] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-311] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-334] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-338] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-312] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-333] for track '28' has 2 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
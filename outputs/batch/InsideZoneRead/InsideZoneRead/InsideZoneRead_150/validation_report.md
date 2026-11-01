# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_150`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_150/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [209–221], lower_priority='Action_ZoneBlock' annotated_start=212, effective_Action_ZoneBlock_start=222.
> - Action 'Action_None' range [209-359] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-312] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-344] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-340] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-284] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-359] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-286] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-265] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-348] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-306] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-353] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-270] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-313] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-286] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-359] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-315] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-232] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [212-273] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [279-280] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-288] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-336] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-241] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [212-270] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-286] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-5] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-323] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-348] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [357-358] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-328] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-345] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-350] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-348] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-352] for track '30' has 1 frames without a visible bounding box.
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
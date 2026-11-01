# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_79`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_79/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [76–84], lower_priority='Action_ZoneBlock' annotated_start=78, effective_Action_ZoneBlock_start=85.
> - Action 'Action_None' range [76-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-186] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-187] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-238] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-150] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-115] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-122] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-129] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-155] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-267] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-236] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-249] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-96] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-153] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-239] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [76-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-164] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [76-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-96] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-134] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-162] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-200] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-264] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-92] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-101] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-152] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-128] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-174] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '26' has 1 frames without a visible bounding box.
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
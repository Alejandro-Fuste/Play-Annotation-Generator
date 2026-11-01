# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_69`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_69/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [264–278], lower_priority='Action_ZoneBlock' annotated_start=267, effective_Action_ZoneBlock_start=279.
> - Action 'Action_None' range [264-307] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-387] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [264-386] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-351] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-361] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-384] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-389] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-301] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [302-327] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [331-377] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [379-380] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [279-293] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [295-338] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [343-353] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [303-342] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [294-301] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-298] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-297] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-263] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-389] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-321] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-333] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-344] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-349] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-365] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-380] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
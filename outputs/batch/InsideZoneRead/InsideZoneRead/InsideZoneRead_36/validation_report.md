# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_36`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_36/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [87–103], lower_priority='Action_ZoneBlock' annotated_start=89, effective_Action_ZoneBlock_start=104.
> - Action 'Action_None' range [87-124] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-211] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-152] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-172] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [128-232] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-140] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-146] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-33] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-63] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-92] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-111] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-189] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [124-131] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-238] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-196] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-200] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-217] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [219-232] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-235] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-233] for track '27' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
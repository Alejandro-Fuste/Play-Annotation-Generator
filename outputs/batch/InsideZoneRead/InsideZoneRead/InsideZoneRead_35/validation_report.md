# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_35`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_35/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [113–128], lower_priority='Action_ZoneBlock' annotated_start=115, effective_Action_ZoneBlock_start=129.
> - Action 'Action_None' range [113-133] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-177] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-134] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-269] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-133] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-267] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-160] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-244] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-185] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-137] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [152-233] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [235-250] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [129-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-269] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-136] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [156-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-128] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-160] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-166] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-204] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-202] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '27' has 1 frames without a visible bounding box.
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
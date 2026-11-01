# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_28`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_28/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '1' (C): higher_priority='Action_BallSnap' [72–89], lower_priority='Action_ZoneBlock' annotated_start=75, effective_Action_ZoneBlock_start=90.
> - Action 'Action_None' range [72-97] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-204] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-147] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-221] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-230] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [120-237] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-203] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [75-141] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-151] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-127] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-201] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-226] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [110-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-195] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-128] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-156] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [75-108] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [75-84] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-170] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [142-177] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-201] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-220] for track '21' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
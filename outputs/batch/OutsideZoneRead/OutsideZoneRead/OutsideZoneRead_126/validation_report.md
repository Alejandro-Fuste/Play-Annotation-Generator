# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_126`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_126/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 22 |
| Ball Tracks | 1 |
| CSV events parsed | 19 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [25–35], lower_priority='Action_ZoneBlock' annotated_start=28, effective_Action_ZoneBlock_start=36.
> - Action 'Action_None' range [25-55] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-113] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-138] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-132] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [64-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [131-155] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [179-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-180] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [25-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-88] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '6' starts at frame 100, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [100-102] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [36-99] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-51] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-82] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-146] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-180] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-33] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-33] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-92] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-77] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-90] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-139] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-179] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '22' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
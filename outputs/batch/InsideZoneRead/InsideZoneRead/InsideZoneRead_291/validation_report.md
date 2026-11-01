# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_291`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_291/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [4–20], lower_priority='Action_ZoneBlock' annotated_start=7, effective_Action_ZoneBlock_start=21.
> - Action 'Action_None' range [4-195] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-194] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [51-111] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [113-449] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-433] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-236] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-230] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-134] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-449] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-444] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-231] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-47] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-121] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-404] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [406-449] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-306] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-30] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-421] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-235] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-314] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-45] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-440] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-259] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-423] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-313] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-121] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-152] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-154] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-254] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-264] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-73] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-157] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-86] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-250] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-205] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-198] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-319] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-331] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-395] for track '32' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
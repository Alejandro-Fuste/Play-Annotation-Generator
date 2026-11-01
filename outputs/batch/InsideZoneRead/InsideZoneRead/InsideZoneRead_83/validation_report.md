# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_83`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_83/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [80–88], lower_priority='Action_ZoneBlock' annotated_start=83, effective_Action_ZoneBlock_start=89.
> - Action 'Action_None' range [80-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-189] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-122] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-190] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-195] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-93] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-153] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [121-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [107-113] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-109] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-115] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-156] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-177] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-154] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-170] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-210] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-153] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-176] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-169] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-194] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-209] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '28' has 1 frames without a visible bounding box.
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
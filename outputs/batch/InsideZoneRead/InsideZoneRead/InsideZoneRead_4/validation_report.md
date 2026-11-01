# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_4`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_4/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 25 |
| Ball Tracks | 1 |
| CSV events parsed | 21 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [86–99], lower_priority='Action_ZoneBlock' annotated_start=88, effective_Action_ZoneBlock_start=100.
> - Action 'Action_ZoneBlock' range [88-122] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-171] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-101] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-214] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-181] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [125-192] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [195-202] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [217-223] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-85] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-227] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-153] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-177] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-56] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-93] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-159] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-233] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '24' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
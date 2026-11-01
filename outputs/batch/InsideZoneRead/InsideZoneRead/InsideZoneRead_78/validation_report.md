# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_78`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_78/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 22 |
| Ball Tracks | 1 |
| CSV events parsed | 20 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [68–82], lower_priority='Action_ZoneBlock' annotated_start=71, effective_Action_ZoneBlock_start=83.
> - Action 'Action_None' range [68-205] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-120] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-114] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [111-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [119-159] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [163-230] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [101-106] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-202] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-159] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-75] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-144] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-211] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-167] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-216] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-222] for track '19' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
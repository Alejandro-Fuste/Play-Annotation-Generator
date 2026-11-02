# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_92`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_92/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 186: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [104–112], lower_priority='Action_ZoneBlock' annotated_start=105, effective_Action_ZoneBlock_start=113.
> - Action 'Action_None' range [104-291] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [127-333] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [338-339] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [343-345] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-328] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-389] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-350] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-355] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-383] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-220] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-231] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-342] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-135] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-288] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-131] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-143] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-323] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-389] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [113-115] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-131] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [105-167] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-199] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [105-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [119-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-355] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-176] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-231] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-331] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-257] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [273-277] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-291] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-346] for track '26' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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
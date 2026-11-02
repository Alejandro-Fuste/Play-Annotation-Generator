# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_201`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_201/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 404: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 404: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 128 frames exceeds threshold 90 frames [start=159, end=286].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (C) duration 128 frames exceeds threshold 90 frames [start=159, end=286].
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [157–172], lower_priority='Action_ZoneBlock' annotated_start=159, effective_Action_ZoneBlock_start=173.
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 128 frames exceeds threshold 90 frames [start=159, end=286].
> - Action 'Action_None' range [157-359] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-312] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-174] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-173] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [159-203] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [206-207] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [211-220] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [222-223] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-321] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [159-238] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [241-258] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [264-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [277-278] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-234] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-345] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-182] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-193] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-273] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-275] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-323] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-333] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-342] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-359] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [157-351] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [353-354] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-250] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-359] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [159-165] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [170-177] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [187-188] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-196] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [219-226] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-45] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-49] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-81] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-86] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-143] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [165-286] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-183] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-214] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-266] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-275] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-290] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-308] for track '25' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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
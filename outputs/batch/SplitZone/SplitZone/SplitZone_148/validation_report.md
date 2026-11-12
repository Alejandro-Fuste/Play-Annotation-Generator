# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_148`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_148/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [131–144], lower_priority='Action_ZoneBlock' annotated_start=134, effective_Action_ZoneBlock_start=145.
> - Action 'Action_None' range [131-215] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-236] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-252] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-189] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-215] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-265] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-172] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [196-204] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-186] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-223] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-295] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [131-171] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [157-168] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [180-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-155] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [158-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [164-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-77] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [131-133] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-189] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-256] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [131-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [152-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [166-186] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [131-168] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-198] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-224] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-278] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-234] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-196] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [138-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-175] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-292] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-205] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-234] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-282] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-267] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-276] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
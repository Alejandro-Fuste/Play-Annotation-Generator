# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_97`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_97/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [111–126], lower_priority='Action_RunBlock' annotated_start=120, effective_Action_RunBlock_start=127.
> - Action 'Action_None' range [111-250] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-288] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-296] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-312] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-316] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [202-224] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-227] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-227] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [127-182] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [223-226] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [120-193] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [128-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-218] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [120-147] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-329] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-223] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-222] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-234] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-223] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-272] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-299] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-312] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-321] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [235-329] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-307] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-315] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-321] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-326] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
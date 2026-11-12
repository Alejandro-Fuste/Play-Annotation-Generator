# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_65`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_65/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [161–176], lower_priority='Action_ZoneBlock' annotated_start=164, effective_Action_ZoneBlock_start=177.
> - Action 'Action_PreSnap' range [0-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-252] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-333] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-359] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-339] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-226] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [191-194] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-359] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-359] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-348] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-359] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-319] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-342] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-228] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-331] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-311] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-349] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
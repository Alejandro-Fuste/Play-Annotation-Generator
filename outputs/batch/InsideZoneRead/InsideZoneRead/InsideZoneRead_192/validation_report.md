# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_192`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_192/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
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
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [145–154], lower_priority='Action_ZoneBlock' annotated_start=147, effective_Action_ZoneBlock_start=155.
> - Action 'Action_None' range [145-287] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-291] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-285] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-212] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-232] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-227] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-275] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-272] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-284] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-283] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-207] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-196] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-202] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [184-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-167] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-279] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-174] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [155-167] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-158] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-188] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [190-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-282] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-301] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-319] for track '27' has 2 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
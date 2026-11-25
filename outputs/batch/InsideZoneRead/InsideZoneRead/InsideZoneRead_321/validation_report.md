# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_321`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_321/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 642: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '8' has invalid range: start=24, end=20. Clamping end to start.
> - Action 'Action_None' range [21-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-109] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-227] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-234] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [70-123] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [127-135] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-137] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-111] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-264] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-179] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [36-165] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-269] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-252] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-264] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-96] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-99] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '25' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_321'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
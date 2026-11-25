# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_226`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_226/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_BallSnap' for track '18' has invalid range: start=203, end=21. Clamping end to start.
> - Action 'Action_None' range [81-195] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-199] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-260] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-136] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-286] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-145] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-193] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-184] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-284] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-134] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-288] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-194] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-204] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [8-50] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-106] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-115] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [5-13] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [5-21] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-131] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-131] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-152] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-219] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-189] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-243] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-249] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-298] for track '21' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_226'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
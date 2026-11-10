# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_20`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_20/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [99-252] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-166] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-249] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-278] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-270] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-298] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [99-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-227] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-250] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-278] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-299] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-162] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-268] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-225] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-143] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-212] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-138] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-240] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-221] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-280] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-241] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-294] for track '26' has 2 frames without a visible bounding box.
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
# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_5`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [52-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-131] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-164] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-177] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-80] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-62] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-80] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-135] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-180] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-114] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-123] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-174] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-171] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-143] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-172] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-66] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-80] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-100] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-137] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-147] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-49] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-86] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-98] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-142] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-123] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-136] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '27' has 1 frames without a visible bounding box.
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
# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_119`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_119/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 220: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [51-81] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-65] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-78] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-94] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-108] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-61] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-99] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-129] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-140] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [51-130] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-277] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-294] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-270] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-294] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-75] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-54] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-137] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-163] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-86] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-94] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-103] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-155] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-298] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-244] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-248] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-264] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-270] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-289] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '30' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
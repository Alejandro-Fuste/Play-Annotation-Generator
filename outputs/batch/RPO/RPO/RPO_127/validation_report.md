# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_127`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_127/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [84-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-164] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-239] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-140] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-144] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-199] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-205] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-228] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-199] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-209] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-228] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-239] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-112] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [157-166] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-239] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-201] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-213] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-207] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-222] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '25' has 1 frames without a visible bounding box.
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
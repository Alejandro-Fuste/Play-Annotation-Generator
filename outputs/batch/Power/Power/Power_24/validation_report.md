# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_24`
- **Input XML**: `outputs/batch/Power/Power/Power_24/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PullBlock' range [96-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [132-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-42] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-193] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-204] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-160] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-164] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-174] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-152] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-163] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-63] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [96-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-174] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-207] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-170] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-101] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-72] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-96] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-158] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-202] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-193] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-201] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-206] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-239] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
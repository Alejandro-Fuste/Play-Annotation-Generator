# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_287`
- **Input XML**: `outputs/batch/Power/Power/Power_287/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [14-306] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-328] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-334] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-276] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-386] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [250-258] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-307] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-314] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-334] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-354] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-381] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [250-270] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-389] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-287] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-317] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-342] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-366] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-389] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-324] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-281] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-296] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [250-255] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-285] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-328] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-321] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-334] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-332] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-285] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-313] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-321] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-325] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-389] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-286] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-284] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-289] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-332] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-344] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-361] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-363] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-354] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-357] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-364] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-372] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [377-387] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-389] for track '28' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
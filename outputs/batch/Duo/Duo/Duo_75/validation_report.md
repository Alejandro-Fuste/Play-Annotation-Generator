# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_75`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_75/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 418 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 418 as fallback play end.
> - Action 'Action_PreSnap' range [0-418] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-369] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [395-403] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [412-416] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-339] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-353] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-378] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-399] for track '3' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-412] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-418] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-317] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-360] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-418] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-323] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-342] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [303-350] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-218] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-371] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-382] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-337] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-353] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-334] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-418] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-418] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-410] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-374] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-392] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-400] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-417] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-322] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-233] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-65] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-313] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-327] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-354] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-361] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-387] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-362] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [390-399] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-399] for track '27' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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
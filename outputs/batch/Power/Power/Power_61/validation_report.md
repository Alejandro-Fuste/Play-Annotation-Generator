# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_61`
- **Input XML**: `outputs/batch/Power/Power/Power_61/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [25-349] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-354] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-278] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-286] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-300] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-369] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-278] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-294] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-334] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-389] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-364] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-311] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-326] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-389] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-280] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-278] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-389] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [260-288] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-257] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-273] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-280] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-293] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [260-273] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [280-303] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [334-335] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-366] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-297] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-323] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-335] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-354] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-376] for track '27' has 1 frames without a visible bounding box.
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
# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_34`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_34/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 24 |
| Ball Tracks | 1 |
| CSV events parsed | 13 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 358 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
> - Action 'Action_PreSnap' range [0-335] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-342] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-347] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-312] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-319] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-351] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-281] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-290] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-342] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-345] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-328] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-358] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-358] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-271] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-248] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-349] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-343] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-122] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [186-258] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '17' starts at frame 263, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [263-263] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-246] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-252] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-294] for track '18' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-301] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-351] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-160] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-244] for track '21' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-358] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-348] for track '23' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
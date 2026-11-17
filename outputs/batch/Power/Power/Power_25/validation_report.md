# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_25`
- **Input XML**: `outputs/batch/Power/Power/Power_25/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [2-282] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-306] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-321] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-326] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-242] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-319] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-327] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-244] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-281] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-285] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-292] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-304] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-165] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-187] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-197] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-204] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-329] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-248] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-270] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-327] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-214] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-226] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-285] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-293] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-316] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-328] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-238] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-329] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-272] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-280] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-284] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-296] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-306] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-328] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-303] for track '26' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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